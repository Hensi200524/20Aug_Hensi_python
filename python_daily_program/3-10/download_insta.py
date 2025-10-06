import instaloader

# Instagram ID
instaID = "harshrajsinh_jadeja_gungan"

# Instaloader object create karo
insta = instaloader.Instaloader()

# Profile download karo
insta.download_profile(instaID, profile_pic_only=False)

print("Download Successfully!")
