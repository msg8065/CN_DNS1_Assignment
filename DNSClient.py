import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '127.0.0.1'
real_name_server = '8.8.8.8'  # Use a valid public DNS server IP address

# Create a list of domain names to query
domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']

# Define a function to query the local DNS server for the IP address of a given domain name
def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answers = resolver.resolve(domain, question_type)
    return answers

# Define a function to query a public DNS server for the IP address of a given domain name
def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.resolve(domain, question_type)
    return answers

# Define a function to compare the results from the local and public DNS servers for each domain name in the list
def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_answers = query_local_dns_server(domain_name, question_type)
        public_answers = query_dns_server(domain_name, question_type)
        if len(local_answers) != len(public_answers):
            return False
        for i in range(len(local_answers)):
            if local_answers[i].to_text() != public_answers[i].to_text():
                return False
    return True

# Define a function to print the results from querying both the local and public DNS servers for each domain name in the domainList
def local_external_DNS_output(domainList, question_type):
    print("Local DNS Server")
    for domain_name in domainList:
        answers = query_local_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {', '.join([answer.to_text() for answer in answers])}")
    print("\nPublic DNS Server")
    for domain_name in domainList:
        answers = query_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {', '.join([answer.to_text() for answer in answers])}")

if __name__ == '__main__':
    # Set the type of DNS query to be performed
    question_type = 'A'
    # Print the results from querying both DNS servers
    local_external_DNS_output(domainList, question_type)
    # Compare the results from both DNS servers and print the result
    result = compare_dns_servers(domainList, question_type)
    print(f"Comparison result: {result}")

