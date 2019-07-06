class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        visits = {}
        for url in cpdomains:
            count = int(url.split(" ")[0])
            domains = url.split(" ")[1].split(".")

            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                visits[domain] = visits.get(domain, 0) + count
                
        output = []
        for visit in visits:
            output.append(str(visits[visit]) + " " + visit)
        return output
