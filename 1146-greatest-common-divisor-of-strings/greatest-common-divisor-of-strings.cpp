class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
       int small = min(str1.size(), str2.size());

        for (int i = small; i >= 1; i--) {
            string x = str1.substr(0, i);

            if (str1.size() % i == 0 && str2.size() % i == 0) {
                string a = "";
                string b = "";

                for (int j = 0; j < str1.size() / i; j++)
                    a += x;

                for (int j = 0; j < str2.size() / i; j++)
                    b += x;

                if (a == str1 && b == str2)
                    return x;
            }
        }

        return ""; 
    }
};