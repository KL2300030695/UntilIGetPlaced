import re

def shortest_segment(text, k, target_words):
    words = re.findall(r'[a-zA-Z]+', text.lower())
    
    target = set(word.lower() for word in target_words)
    
    window_count = {}
    left = 0
    matched = 0
    
    min_len = float('inf')
    result = None
    
    for right in range(len(words)):
        word = words[right]
        
        if word in target:
            window_count[word] = window_count.get(word, 0) + 1
            
            if window_count[word] == 1:
                matched += 1
        
        while matched == len(target):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = (left, right)
            
            left_word = words[left]
            
            if left_word in target:
                window_count[left_word] -= 1
                if window_count[left_word] == 0:
                    matched -= 1
            
            left += 1
    
    if result is None:
        return "NO SUBSEGMENT FOUND"
    
    l, r = result
    return " ".join(words[l:r+1])