class Solution(object):
    def compress(self, chars):
        walker, runner = 0, 0

        while runner < len(chars):
            char = chars[runner]
            count = 0

            
            while runner < len(chars) and chars[runner] == char:
                runner += 1
                count += 1

            
            chars[walker] = char
            walker += 1

            
            if count > 1:
                for c in str(count):
                    chars[walker] = c
                    walker += 1

        return walker