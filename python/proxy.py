# Interface for search service
class SearchService:
    def search(self, query):
        pass

# Secondary Memory Class
class SearchMainMemory(SearchService):
    def search(self, query):
        return f"Searching in secondary memory for query: {query}"

# Proxy Memory Class
class ProxyMemory(SearchService):
    def __init__(self, user):
        self.user = user
        self.secondary_memory = SearchMainMemory()

    def search(self, query):
        if self.user == "admin":
            # Authorized user (admin) can access secondary memory
            return self.secondary_memory.search(query)
        else:
            return "Access denied. You do not have the necessary privileges."

# Example usage
admin_proxy = ProxyMemory(user="admin")
user_proxy = ProxyMemory(user="user")

query = "Your search query"

# Search in secondary memory (admin)
print(admin_proxy.search(query)) 
# Access denied (user)
print(user_proxy.search(query))  
