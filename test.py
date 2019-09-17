from pythaisa import *
datatrain=[("ฉันรักคุณ","love"),("ผมก็รักคุณเหมือนกัน","love"),("เกลียดคุณ","neg"),("เกลียดเหมือนกัน","neg")]
m=model(name="test",train_dataset=datatrain)
m.train()
print(m.predict("ฉันรักคุณ"))