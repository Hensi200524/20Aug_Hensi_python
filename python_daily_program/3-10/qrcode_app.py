# import instaloader

# instaID="topstech"

# insta=instaloader.Instaloader()
# insta.download_profile(instaID)
# print("Download Successfully!")

import qrcode

url = "https://www.tops-int.com/"

qr = qrcode.make(url)
qr.save("tops.png")

print("✅ QR code generated successfully: tops.png")
