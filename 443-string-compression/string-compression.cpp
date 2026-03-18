class Solution {
public:
    int compress(vector<char>& chars) {
        int n = chars.size();
        int index = 0;

        // Iterate through the array to group repeated characters
        for(int i = 0; i < n; i++) {
            char ch = chars[i]; // Current character being compressed
            int count = 0;

            // Count how many times the character repeats
            while(i < n && chars[i] == ch) {
                count++; i++;
            }

            // If character doesn't repeat don't add a count 
            if(count == 1) {
                chars[index++] = ch;
            } else {
                // Character does repeat adjust the count
                chars[index++] = ch;
                string str = to_string(count);

                // Write each count of the digit in the array
                for(char dig : str) {
                    chars[index++] = dig;
                }
            }
            i--;
        }
        // Resize the array to the new compressed length
        chars.resize(index);
        return index;
    }
};