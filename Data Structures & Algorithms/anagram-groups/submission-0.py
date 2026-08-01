class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = {}
        for ele in strs:
            sort_str = "".join(sorted(ele))
            if sort_str not in grp_anagrams:
                grp_anagrams[sort_str] = []
                grp_anagrams[sort_str].append(ele)
            else:
                grp_anagrams[sort_str].append(ele)
        return list(grp_anagrams.values())
        