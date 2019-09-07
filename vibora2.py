RUN apk add py-pip
import asyncio
from vibora import Vibora
from vibora.request import Request
from vibora.responses import JsonResponse

app = Vibora()


@app.route('/')
def home():
    return JsonResponse({'hello': 'world'})


@app.route('/async', methods=['GET'])
async def home_async(request: Request):
    await asyncio.sleep(1)
    print(request.headers)
    return JsonResponse({'hello': 'world'}, status_code=201)


if __name__ == '__main__':
    app.run()