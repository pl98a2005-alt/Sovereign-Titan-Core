import os
import shutil

def factory_clean_up():
    """تنظيف الملفات الزائدة مع الإبقاء على الضروريات"""
    print("🧹 Starting Factory Clean-up...")
    
    # المجلدات التي يجب حمايتها (لا تلمسها)
    protected = ['vault', 'core', 'games', 'concepts']
    
    # حذف الملفات المؤقتة والمجلدات غير الضرورية في الجذر
    for item in os.listdir('.'):
        if item not in protected and item != 'main.py' and item != 'requirements.txt':
            if os.path.isfile(item):
                os.remove(item)
                print(f"🗑️ Deleted file: {item}")
            elif os.path.isdir(item) and not item.startswith('.'):
                shutil.rmtree(item)
                print(f"🗑️ Deleted folder: {item}")
                
    print("✨ Clean-up Complete. System is optimized.")

