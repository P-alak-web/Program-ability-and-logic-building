def groupAnagrams(strs):
    anagram_map = {}

    for word in strs:
        # Sort the word to use as a key
        key = ''.join(sorted(word))
        
        if key not in anagram_map:
            anagram_map[key] = []
        
        anagram_map[key].append(word)

    return list(anagram_map.values())


# -------------------------
# Example 1
strs1 = ["eat","tea","tan","ate","nat","bat"]
print("Example 1 Output:")
print(groupAnagrams(strs1))

# -------------------------
# Example 2
strs2 = [""]
print("\nExample 2 Output:")
print(groupAnagrams(strs2))

# -------------------------
# Example 3
strs3 = ["a"]
print("\nExample 3 Output:")
print(groupAnagrams(strs3))