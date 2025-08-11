import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def gutendex_proxy(request, gutenberg_id):
    gutendex_url = f'https://gutendex.com/books/{gutenberg_id}'
    try:
        res = requests.get(gutendex_url, timeout=5)
        res.raise_for_status()
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_502_BAD_GATEWAY)

    return Response(res.json())

@api_view(['GET'])
def gutendex_search(request):
    query = request.GET.get("q", "").strip()
    gutendex_url = f"https://gutendex.com/books?search={query}"
    try:
        res = requests.get(gutendex_url, timeout=5)
        res.raise_for_status()
    except requests.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_502_BAD_GATEWAY)

    return Response(res.json())
