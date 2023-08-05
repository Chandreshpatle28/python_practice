cloud_providers = ["AWS","GCP","Azure"]

print("Before Append: ", cloud_providers)

cloud_providers.append("Digital Ocean")

print("After Append: ", cloud_providers)

cloud_providers.sort()

print("Sorted List of Cloud Providers :", cloud_providers)
