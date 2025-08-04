"""class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
    for str1 in strs:
        keys=" ".join(sorted(str1))
        if key not in hashmap:
            hashmap[key]=[]
            hashmap[key].append(str1)
    return list(hashmap.values())"""
class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)
        return list(hashmap.values())  # <- This line is now properly indented!            







        


        