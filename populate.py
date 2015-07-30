# -*- coding: utf-8 -*-
import xml.etree.ElementTree as etree
import os
import django
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'cgm.settings')

django.setup()
from tree import models

from django.core.files import File
import urllib.request
from django.conf import settings


def save_img(entry, path, img_filename):

    response = urllib.request.urlopen(path)
    with open('tmp_img', 'wb') as f:
        f.write(response.read())

    with open('tmp_img', 'rb') as f:
        img_file = File(f)
        entry.image_product.save(img_filename, img_file, True)
    os.remove('tmp_img')


def parse_id(id):
    return int(str(ord(id[0])) + id[1:])


def del_l(t):
    return t.replace('~', ' ')


def my_parse():

    models.User_rezult.objects.all().delete()
    models.Answer.objects.all().delete()
    models.Questions.objects.all().delete()
    models.Property_char.objects.all().delete()
    models.Products.objects.all().delete()
    models.Products_property.objects.all().delete()
    models.Tying_products.objects.all().delete()
    models.Relations_tying_products.objects.all().delete()

    bay = models.Tying_products(id = 1 ,name="Приходите еще")
    bay.save()
    
    tying_product_case = models.Tying_products(name="Чехол кожаный", price = 2000)
    tying_product_case.save()

    tying_product_garanty = models.Tying_products(name="Доп. гарантия", price =1000)
    tying_product_garanty.save()

    tying_product_mambrace = models.Tying_products(name="Защитная пленка", price =200)
    tying_product_mambrace.save()

    oper_system = models.Property_char(
        name_property_char="oper_system", name_property_trans='OS')
    oper_system.save()
    screen_size = models.Property_char(
        name_property_char="screen_size", name_property_trans='Size')
    screen_size.save()
    foto = models.Property_char(
        name_property_char="foto", name_property_trans='Foto')
    foto.save()
    internet = models.Property_char(
        name_property_char="internet", name_property_trans='Интернет')
    internet.save()
    # --------------------------------------------------------------------------------
    description = "Nokia 106 Black Форм-фактор/Моноблок|Управление/Кнопки|Материал корпуса/Пластик|Стандарты связи, (МГц)/GSM 900/1800|Количество сим-карт/1 слот для сім-карти|Тип дисплея/TFT|Количество цветов дисплея/65 тыс. |Разрешение дисплея/160x128|Диагональ дисплея/1, 8"

    product = models.Products(name='Nokia 1100', description=description,price = 400)
    product.save()

    relate = models.Relations_tying_products(product=product,
                                             tying_product=tying_product_case)
    relate.save()
    models.Relations_tying_products(product=product,
                                    tying_product=tying_product_garanty)
    relate.save()

    save_img(
        product, "file://" + settings.MEDIA_ROOT + "/nokia-1100.png", u"Nokia1100")

    el_prop = models.Products_property(products=product, name_property=oper_system,
                                       value_property='Нет')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=screen_size,
                                       value_property='1.8')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=foto,
                                       value_property='Нет')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=internet,
                                       value_property='Нет')
    el_prop.save()
    # --------------------------------------------------------------------------------
    description = "Смартфон Samsung Galaxy S6 - не просто эволюционное развитие линейки флагманских устройств от корейского производителя. Шестое поколение устройств Galaxy S является полным переосмыслением дизайна, используемых материалов корпуса и функциональности. На место пластика пришло сочетание стекла и металла, смартфон получил неразборный корпус повышенной жесткости, отсутствие съемных деталей обеспечивает полную монолитность конструкции. Дисплей флагмана выполнен по технологии Super AMOLED с разрешением 2560х1440, что в сочетании с диагональю в 5,1 дюйма обеспечивают феноменальный показатель четкости - 577 точек на дюйм. Плавную и быструю работу Samsung Galaxy S6 обеспечивает наиболее производительная система-на-чипе Samsung Exynos 7420 состоящая из двух четырехъядерных вычислительных ядер Cortex-A53/A57 с поддержкой 64-битных вычислений. Фотографические способности так же достойны флагмана, основная камера получила модуль с максимальным разрешением 16 МП и возможностью записи видео в разрешении 2160р. Фронтальная камера порадует любителей селфи и выводит автопортреты на новый качественный уровень благодаря диафрагме f/1.9. Емкость аккумулятора не может похвастаться рекордными значениями, однако главным козырем Samsung Galaxy S6 является достижение необходимого уровня заряда для 4 часов работы за 10 минут."
    product = models.Products(
        name='Samsung Galaxy S6', description=description,price = 24000)
    product.save()

    models.Relations_tying_products(product=product,
                                    tying_product=tying_product_garanty)
    relate.save()

    save_img(
        product, "file://" + settings.MEDIA_ROOT + "/Samsung-Galaxy-S6-Edge-3.png", u"Galaxy")
    el_prop = models.Products_property(products=product, name_property=oper_system,
                                       value_property='Android')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=screen_size,
                                       value_property='5.1')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=foto,
                                       value_property='Да')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=internet,
                                       value_property='Да')
    el_prop.save()
    # --------------------------------------------------------------------------------
    description = 'Blackberry Z10 - смартфон от всемирно известной компании RIM, сменившей название на более привычное пользователям Blackberry. Устройство работает под управлением фирменной операционной системы Blackberry 10, полностью переработанной и ориентированной на сенсорное управление. Blackberry Z10 оборудован 4.2 дюймовым экраном с разрешением 1280х768 точек. Насладитесь четкостью изображения во время браузинга или просмотра фото и видео. Смартфон построен на 2-ядерной платформе Snapdragon S4, дополненной интегрированным видеочипом Adreno 225 и 2 ГБ оперативной памяти. Производительности Blackberry Z10 достаточно для того, чтобы легко справляться с любыми задачами пользователя.'
    product = models.Products(name='BlackBerry Z10', description=description,price = 18500)
    product.save()

    relate = models.Relations_tying_products(product=product,
                                             tying_product=tying_product_case)
    relate.save()

    relate = models.Relations_tying_products(product=product,
                                             tying_product=tying_product_garanty)
    relate.save()

    relate = models.Relations_tying_products(product=product,
                                             tying_product=tying_product_mambrace)
    relate.save()

    save_img(
        product, "file://" + settings.MEDIA_ROOT + "/Z10_black_ENG_Gen_FrontAngle.png", u"Blackberry")
    el_prop = models.Products_property(products=product, name_property=oper_system,
                                       value_property='BlackBerry OS10')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=screen_size,
                                       value_property='4.2')
    el_prop.save()
    el_prop = models.Products_property(products=product, name_property=foto,
                                       value_property='Да')
    el_prop.save()

    el_prop = models.Products_property(products=product, name_property=internet,
                                       value_property='Да')
    el_prop.save()
    # --------------------------------------------------------------------------------
    tree = etree.parse('Game_01.xml')

    root = tree.getroot()
    for level in root:  # levels

        Id = parse_id(level.find('Id').text)
        # import pdb; pdb.set_trace()
        for Questions in level.iter('Questions'):
            for Question in Questions.iter('Question'):

                text_answer = ''.join(
                    Question.find('Text').text)

                text_answer = del_l(text_answer)
                # print(str(Question.find('Text').text))
                answer_model = models.Answer(id=Id, text_answer=text_answer)
                answer_model.save()
                for Answers in Question.iter('Answers'):
                    for Answer in Answers.iter('Answer'):

                        id_question = int(
                            str(Id) + str(parse_id(Answer.find('Id').text)))

                        text_question = ''.join(
                            Answer.find('Text').text)
                        if str(id_question) == '1082397001' or str(id_question)[3:6] == '1081597001' \
                                or str(id_question)[3:6] == '1081497001' or str(id_question)[3:6] == '1081397001':
                            text_question = 'Предложить товар'

                        else:
                            text_question = del_l(text_question)
                        target = parse_id(Answer.find('Target').text)
                        point = int(Answer.find('Point').text)

                        question_model = models.Questions(id=id_question, point_answer=point,
                                                          text_questions=text_question, relation_answer=answer_model,
                                                          question_answer=target)
                        question_model.save()

    ess_prop = models.Essential_prop(
        relation_answer_id=10810, name_property=internet, value_property='Да')
    ess_prop.save()

    model_zdrav = models.Answer.objects.get(id=1081)
    test_quest = models.Questions(point_answer=50, point_emotions=-30,
                                  text_questions="Предложить товар",
                                  relation_answer=model_zdrav, question_answer=48)
    test_quest.save()

    el_quest = models.Questions.objects.get(id=1081397001)
    el_quest.text_questions = "Предложить товар"
    el_quest.save()

    el_quest = models.Questions.objects.get(id=1081497001)
    el_quest.text_questions = "Предложить товар"
    el_quest.save()

    el_quest = models.Questions.objects.get(id=1081597001)
    el_quest.text_questions = "Предложить товар"
    el_quest.save()

    el_quest = models.Questions.objects.get(id=1082197001)
    el_quest.text_questions = "Предложить товар"
    el_quest.save()

    # mod_ans = models.Answer(id=48, text_answer="Выход")
    # mod_ans.save()
    # mod_ans = models.Answer(id=47, text_answer="Что вы мне хотите предложить?")
    # mod_ans.save()
    # mod_bay = models.Answer(id=47, text_answer="Попрощаться")
    # mod_bay.save()

    
    
    return True

if __name__ == "__main__":
    print(my_parse())
