#include "yaml-cpp/yaml.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    string fileName = "../sample.yaml";
    cout << fileName << endl;

    std::ofstream fout(fileName);
    // YAML::Node node = YAML::LoadFile(fileName);

    YAML::Emitter out;
    out << YAML::BeginSeq;
    out << "eggs";
    out << "bread";
    out << "milk" << YAML::EndSeq;

    out << YAML::BeginMap;
    out << YAML::Key << "name";
    out << YAML::Value << "Ryan Braun";
    out << YAML::Key << "position";
    out << YAML::Value << "LF";
    // out << YAML::EndMap;


    // out << YAML::BeginMap;
    out << YAML::Key << "name";
    out << YAML::Value << "Barack Obama";
    out << YAML::Key << "children";
    out << YAML::Value << YAML::BeginSeq << "Sasha" << "Malia" << YAML::EndSeq;
    out << YAML::EndMap;

    fout << out.c_str();

    return 0;
}