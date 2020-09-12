from os import environ

BANANO_HTTP_PROVIDER_URI = environ.get(
    "BANANO_HTTP_PROVIDER_URI", "https://api-beta.banano.cc"
)
BANANO_NODE_PORT = environ.get("BANANO_NODE_PORT", 443)

PIPPIN_HTTP_PROVIDER_URI = environ.get(
    "PIPPIN_HTTP_PROVIDER_URI", ""
)
PIPPIN_PORT = environ.get("PIPPIN_PORT", 11338)

BANANO_API = f"{BANANO_HTTP_PROVIDER_URI}:{BANANO_NODE_PORT}"

if PIPPIN_HTTP_PROVIDER_URI == "":
    PIPPIN_API = False
else:
    PIPPIN_API = f"{PIPPIN_HTTP_PROVIDER_URI}:{PIPPIN_PORT}"

print(f"Using {BANANO_HTTP_PROVIDER_URI} as API provider on port {BANANO_NODE_PORT}")
if not PIPPIN_API:
    print(f"Pippin not in use")
else:
    print(f"Using {PIPPIN_HTTP_PROVIDER_URI} as Pippin provider on port {PIPPIN_PORT}")
