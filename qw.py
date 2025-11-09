from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pub = priv.public_key()
message = b"Important message to sign"
signature = priv.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)
print("Signature (hex):", signature.hex())
try:
    pub.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature is VALID")
except Exception as e:
    print("Signature verification FAILED:", e)