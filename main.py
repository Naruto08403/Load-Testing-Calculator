from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
def index():
    return 'This calculator api works'

@app.get('/solve')
def solve(express:str):
    express = express.lower().replace(' ','+').replace('x','*')
    print(express)
    
    try:
        answer = eval(express)
        return {'expression':express,"answer":answer}
    except Exception as e:
        return {'error':str(e)}

if __name__ == '__main__':
    uvicorn.run(app)