"""This script consist of the class LidarScan which does some functionalities for Lidar+Image Fusion DL Network."""
import numpy as np
import pandas as pd


class LidarScan():
    """Class that contain Lidar pointcloud values timestamp, x, y, z, Intenstiy ."""
    
    EXTENSIONS_SCAN = ['.csv']

    def __init__(self,
                 project=False,
                 H=64,
                 W=1024,
                 fov_up=2.0,
                 fov_down=-24.8):
        """Initialisation of base attributes."""
        self.project = project
        self.project_H = H
        self.project_W = W
        self.project_fov_up = fov_up
        self.project_fov_down = fov_down
        self.reset()

    def reset(self):
        """Reset (Set Dummy values) scan members."""
        self.points = np.zeros((0, 3), dtype=np.float)        # [m, 3]: x, y, z
        self.intensity = np.zeros((0, 1), dtype=np.float)     # [m ,1]: intensity

        # projected range image - [H,W] range (-1 is no data)
        self.proj_range = np.full((self.project_H, self.project_W),
                                  -1,
                                  dtype=np.float)

        # unprojected range (list of range for each point)
        self.unproj_range = np.zeros((0, 1), dtype=np.float)

        # projected point cloud xyz - [H,W,3] xyz coord (-1 is no data)
        self.proj_xyz = np.full((self.project_H, self.project_W, 3), -1,
                                dtype=np.float)

        # projected intensity - [H,W] intensity (-1 is no data)
        self.proj_intensity = np.full((self.project_H, self.project_W),
                                      -1,
                                      dtype=np.float)

        # projected index (for each pixel, what I am in the pointcloud)
        # [H,W] index (-1 is no data)
        self.proj_idx = np.full((self.project_H, self.project_W),
                                -1,
                                dtype=np.int32)

        # for each point, where it is in the range image
        self.project_x = np.zeros((0, 1), dtype=np.int32)        # [m, 1]: x
        self.project_y = np.zeros((0, 1), dtype=np.int32)        # [m, 1]: y

        # mask containing for each pixel, if it contains a point or not
        self.proj_mask = np.zeros((self.project_H, self.project_W),
                                  dtype=np.int32)                # [H,W] mask

    def read_pointcloud_csv(self,
                            file_path='*.csv'):
        """Read the Point cloud data from a given csv input file."""
        pc_data = pd.read_csv(file_path,
                              dtype=float)
        pc_data = np.array(pc_data[['ts_global','x','y','z','intensity_cal']])
        return pc_data

    def convert_Lidar_to_FV_Image(self,
                                  point_cloud_data=pc_data):
        """Project a 3D Lidar point cloud data into a 2D Front view using Spherical Projection."""
        #  For Velodyne HDL 64-E
        #  Fov_Up                               =  02   degrees
        #  Fov_Down                             = -24.8 degrees
        #  Num of Lasers                        =  64
        #  Best length of image comes out to be = 1024
        
        # Extact Time stamp
        self.time_stamp = point_cloud_data[:,0]

        # Extact the Intensity of detection
        self.intensity = point_cloud_data[:,4]

        # Get the Points (x,y,z)
        self.points = point_cloud_data[:,1:4]

        # Extact the x,y,z coordinates
        point_x = self.points[:,0]
        point_y = self.points[:,1]
        point_z = self.points[:,2]

        # Laser parameters
        fov_up = (self.project_fov_up / 180.0) * np.pi      # field of view up in rad
        fov_down = (self.project_fov_down / 180.0) * np.pi  # field of view down in rad
        fov = abs(fov_down) + abs(fov_up)  # get field of view total in rad

        # get Range of all points
        range = np.linalg.norm(self.points, 2, axis=1)

        # get angles of all points
        pitch = np.arcsin(point_z / range)
        yaw = -np.arctan2(point_y, point_x)

        # get projections in image coords
        project_x = 0.5 * ((yaw / np.pi) + 1.0)               # in [0.0, 1.0]
        project_y = 1.0 - ((pitch + abs(fov_down)) / fov)     # in [0.0, 1.0]

        # scale to image size using angular resolution
        project_x *= self.project_W                              # in [0.0, W]
        project_y *= self.project_H                              # in [0.0, H]

        """ 
        - This procedure results in a list of (u, v) tuples (project_x, project_y) 
        containing a pair of image coordinates for each 'point[i]' , which we 
        use to generate our proxy representation.
        - Using these indexes, we extract for each point[i] its 'range', its x,y,z coordinates,
        and 'intensity', and we store them in the image, creating a
        [5 × h × w] tensor. 
        - Because of the de-skewing of the scan, the assignment of each points to its corresponding 
        (u, v) is done in a descending range order, to ensure that all points rendered in the image 
        are in the current field of view of the sensor.
        """
        # round and clamp for use as index
        project_x = np.floor(project_x)
        project_x = np.minimum(self.project_W - 1, project_x)
        project_x = np.maximum(0, project_x).astype(np.int32)   # in [0,W-1]
        self.project_x = np.copy(project_x)                     # store a copy in orig order

        project_y = np.floor(project_y)
        project_y = np.minimum(self.project_H - 1, project_y)
        project_y = np.maximum(0, project_y).astype(np.int32)   # in [0,H-1]
        self.project_y = np.copy(project_y)                     # stope a copy in original order

        # copy of range in original order
        self.unproj_range = np.copy(range)

        # order in decreasing range
        indices = np.arange(range.shape[0])
        order = np.argsort(range)[::-1]
        range = range[order]
        indices = indices[order]
        points = self.points[order]
        intensity = self.intensity[order]
        project_y = project_y[order]
        project_x = project_x[order]

        # assign to images
        self.proj_range[project_y, project_x] = range
        self.proj_xyz[project_y, project_x] = points
        self.proj_intensity[project_y, project_x] = intensity
        self.proj_idx[project_y, project_x] = indices
        self.proj_mask = (self.proj_idx > 0).astype(np.int32)

if __name__ == "__main__":
    csv_file_path = "/home/girsur/workspace/sample.csv"
    lidarsweep = LidarScan()
    pc_data = lidarsweep.read_pointcloud_csv(csv_file_path)
    lidarsweep.convert_Lidar_to_FV_Image(pc_data)