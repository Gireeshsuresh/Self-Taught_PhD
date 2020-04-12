class Solution:
    def stringMatching(self,words):
        words.sort()
        # print(words)
        dummy = []
        for c in words:
            co = 0
            
            # print("C = ", c)
            for i in range(0,len(words)):
                # print("I = ", i)
                # print("W = ", words[i])
                if c in words[i]:
                    co = co + 1
                    # print("CO = ", co)
                    if(co>1):
                        dummy.append(c)
                        # print("Dummy = ", dummy)
                        # print (" ")
                        co = 0
                        break
        return dummy

if __name__ == "__main__":
    l = ["mass", "as", "hero", "superhero"]
    d = []
    od = Solution()
    d = od.stringMatching(l)
    print(d)