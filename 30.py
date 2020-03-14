from collections import Counter
class Solution:
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == "" or words == []:
            return [];
        step = len(words[0]);
        num = len(words);
        ws = step * num;
        left = 0;
        required = Counter(words)
        formed = {}
        ans = []
        i = 0;
        while(i < step):
            left = i;
            #initialize 
            s_s = s[left:left + step*num+1];
            j = 0;
            while(j < num):
                phase = s_s[j*step:(j+1)*step];
                formed[phase] = formed.get(phase,0) + 1;
                j += 1;
            #print(len(formed.values()))
            if formed == required:
                ans.append(left);
            #move the window
            
            while(left < len(s) - step*num):
                formed[s[left:left+step]] -= 1;
                if formed[s[left:left+step]] == 0:
                    formed.pop(s[left:left+step]);
                left += step;
                phase = s[left+(num-1)*step:left+num*step]
                formed[phase] = formed.get(phase,0) + 1;
                #print(formed)
                if formed == required:
                    ans.append(left);
            formed = {};#reset the hash map before enter the next loop
            i += 1;
            
        return ans;
           
