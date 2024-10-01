import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

# if __name__ == "__main__":
#     def convert(s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         result = ""
#         max_l = 2 * (numRows - 1)
#         for i in range(numRows):
#             x = 2 * (numRows - 1 - i)
#             y = max_l - x
#
#             if i < len(s):
#                 result = result + s[i]
#
#             curr_index = i
#             while curr_index < len(s):
#
#                 if x != 0:
#                     curr_index = curr_index + x
#                     if curr_index >= len(s):
#                         break
#
#                     result = result + s[curr_index]
#
#                 if y != 0:
#                     curr_index = curr_index + y
#                     if curr_index >= len(s):
#                         break
#
#                     result = result + s[curr_index]
#
#         return result
#
#     result = convert("PAYPALISHIRING", 3)
#     print(result)
