Pytest Decorator 


Pytest, Python dilinde yazılmış bir test çerçevesidir. Test senaryolarınızı (test fonksiyonlarınızı) çalıştırmanıza, organize etmenize ve raporlamanıza olanak tanır. Pytest, standart Python unittest modülüne kıyasla daha basit ve daha esnek bir kullanım sunar.

Pytest decorator'ları, test senaryolarının davranışını ve özelliklerini değiştirmek için kullanılır. Pytest'in özelliklerinden biri, decorator'ların kullanımıdır. Decorator'lar, test fonksiyonlarının özelliklerini değiştirmek veya genişletmek için kullanılabilir. Bu, testlerin daha okunaklı ve anlaşılır hale gelmesini sağlar.

Pytest decorator'ları şunları içerebilir:

@pytest.fixture => Test senaryolarında kullanılacak tekrar eden işlemleri tanımlamak için kullanılır. Örneğin, bir veritabanına bağlanmak veya bir dosya okumak gibi.

@pytest.mark.parametrize => Test senaryolarının farklı parametrelerde çalıştırılmasını sağlamak için kullanılır.

@pytest.mark.skip => Belirli bir test senaryosunun geçiçi olarak atlanmasını sağlar.

@pytest.mark.xfail => Bir test senaryosunun özellikle başarısız olması bekleniyorsa, bunu belirtmek için kullanılır.

@pytest.mark.timeout => Bir test senaryosunun belirli bir süre içinde tamamlanması gerektiğini belirtmek için kullanılır.

@pytest.mark.filterwarnings => Test senaryolarında belirli bir uyarı mesajının beklenen olduğunu belirtmek için kullanılır.
