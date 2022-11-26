import heapq

languages = ["Python", "Java", "C++", "C", "C#", "JavaScript"]
heapq.heapify(languages)
heapq.heappush(languages, "A")

heapq.heappop(languages)
heapq.heappop(languages)
heapq.heapreplace(languages, "Z")
print(languages)

ages = [12,20,24,1,45,26,14]
heapq.heapify(ages)
print(ages)

#print(heapq.nlargest(4, ages))
#print(heapq.nsmallest(4, ages))

#heapq.heappushpop(ages, 100)
#heapq.merge([100,200],[250,360,3])

