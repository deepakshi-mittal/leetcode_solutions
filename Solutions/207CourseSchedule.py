class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # course which have nomout edge means dont have any prerequisite
        # https://www.youtube.com/watch?v=EgI5nU9etnU&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=3
        
        
        pre_map = {crs_num: [] for crs_num in range(numCourses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        
        # print(pre_map)
            
        visited_set = set()
        
        def dfs(current_course):
            if current_course in visited_set:
                return False   # loop here
            if pre_map[current_course] == []:
                return True
            
            visited_set.add(current_course) # add to visted set before doing dfs
            
            for pre_req in pre_map[current_course]:
                if not dfs(pre_req):
                    return False
            visited_set.remove(current_course)  #remove current_course to visted set after doing dfs
            pre_map[current_course] = [] # important step to avoid TLE
            return True
        
        for course in pre_map: 
            # needed because grapgh can be disconnected
            if not dfs(course):
                return False
        
        return True
