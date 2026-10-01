class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mlist = defaultdict(list)
        for w in strs:
            sortedS = ''.join(sorted(w))
            mlist[sortedS].append(w)
        return list(mlist.values())
        