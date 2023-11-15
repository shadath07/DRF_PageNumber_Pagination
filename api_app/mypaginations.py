from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    # This is usedas if we want to search using p instead of writinh search keyword 
    page_query_param = 'p'
    # This is used as if you to give the client to set the page size how how he wants to see in the page 
    page_size_query_param ='records'
    # This line is used to set the limit for a page to display the max number of size.
    max_page_size = 7
    