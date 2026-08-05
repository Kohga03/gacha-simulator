from flask import Flask,render_template,request
import random
app=Flask(__name__)
chars={"SSR":["勇者","魔王","天使"],"SR":["騎士","魔法使い","忍者","エルフ"],"R":["スライム","ゴブリン","村人","商人","犬","猫"]}
history=[]
character_count={c:0 for rs in chars.values() for c in rs}
def draw():
    x=random.random()
    r="R"
    if x<0.03:r="SSR"
    elif x<0.20:r="SR"
    c=random.choice(chars[r]);history.append((r,c));character_count[c]+=1;return r,c
@app.route("/",methods=["GET","POST"])
def index():
    results=[]
    if request.method=="POST":
        n=10 if request.form["mode"]=="10" else 1
        for _ in range(n):results.append(draw())
    total=len(history);ssr=sum(1 for r,_ in history if r=="SSR");rate=ssr/total*100 if total else 0
    return render_template("index.html",results=results,history=history[::-1],total=total,ssr=ssr,rate=rate,chars=chars,character_count=character_count)
app.run(host="0.0.0.0",port=5000)
