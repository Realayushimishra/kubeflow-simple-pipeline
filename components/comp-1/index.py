import types
import marshal

s = open("fake.pye", 'rb')
s.seek(16) # Ignore first 16 bytes for some reason

module = marshal.load(s)

fake = types.ModuleType("Fake", "fake")

exec(module, fake.__dict__)

print(fake.fake_name())

print(fake.fake_email())

print(fake.fake_address())
