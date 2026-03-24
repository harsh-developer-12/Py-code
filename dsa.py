# queue = []

# queue.append(1)
# queue.append(9)
# queue.append(3)
# print("queue:", queue)
# q= queue.pop(2)
# print("after queue:" , q)
# print(queue)

# w= len(queue) == 0
# print("is queue empty?", w)



from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask working!"

app.run(debug=True)

