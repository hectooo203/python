srv_a = {22, 80, 443, 3306, 8080}
srv_b = {22, 443, 5432, 8080, 9000}

print(f"{srv_a & srv_b}, {srv_a - srv_b}, {len(srv_a | srv_b)} puertos, {3306 in srv_b}")