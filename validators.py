import re

# قائمة سوداء أولية للعلامات التجارية (يمكن توسيعها)
BLACKLIST = ['amazon', 'meta', 'bitcoin', 'whatsapp', 'google', 'apple', 'facebook']

def check_trademark(keyword, blacklist=BLACKLIST):
    """
    تحقق إذا كانت الكلمة تحتوي على علامة تجارية محظورة.
    إرجاع True إذا كانت آمنة، False إذا كانت محظورة.
    """
    for brand in blacklist:
        if re.search(brand, keyword, re.IGNORECASE):
            return False
    return True

def clean_special_chars(keyword):
    """
    إزالة الرموز الخاصة والأرقام غير المرغوبة باستخدام Regex.
    """
    return re.sub(r'[^a-z0-9]', '', keyword)  # يحتفظ فقط بأحرف صغيرة وأرقام
