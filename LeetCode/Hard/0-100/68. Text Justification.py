class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i<n:
            # 1. 找这一行能放多少单词
            j = i
            line_len = 0
                            #这部分是：当前长度 + 单词长度 + 空格数 ≤ maxWidth
            while j<n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            
            # 当前行 words[i:j]
            gaps = j - i -1
            line = ""
            # 2. 判断是不是最后一行 or 单词数=1
            if j==n or gaps == 0:
                #左对齐
                line = " ".join(words[i:j])
                line+= " " * (maxWidth - len(line))
            else:
                # 3. 均匀分配空格
                total_spaces = maxWidth - line_len
                avg = total_spaces // gaps
                extra = total_spaces % gaps

                for k in range(i,j-1):
                    line += words[k]
                    spaces = avg + (1 if k - i < extra else 0)
                    line += " " * spaces
                
                line += words[j - 1]  # 最后一个词

            res.append(line)
            i = j
        
        return res