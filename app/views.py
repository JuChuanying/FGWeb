'''
定义路由和视图函数
'''
import os
from flask import Blueprint, render_template, request,jsonify, current_app, url_for
from werkzeug.utils import secure_filename
# from model.model import run_model  # 假设你有一个函数来处理模型逻辑

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():
    if 'sourceImage' not in request.files or 'referenceImage' not in request.files:
        return jsonify({'error': 'No file part'})

    source_image = request.files['sourceImage']
    reference_image = request.files['referenceImage']

    if source_image.filename == '' or reference_image.filename == '':
        return jsonify({'error': 'No selected file'})

    if source_image and reference_image:
        try:
            # Save the files securely
            source_filename = secure_filename(source_image.filename)
            reference_filename = secure_filename(reference_image.filename)
            source_image_path = os.path.join('/home/d/jcy/Web/FGWeb/app/static', 'uploads', source_filename)
            reference_image_path = os.path.join('/home/d/jcy/Web/FGWeb/app/static', 'uploads', reference_filename)

            print(f'{source_filename},{source_image_path}')
            print(f'{reference_filename},{reference_image_path}')

            source_image.save(source_image_path)
            reference_image.save(reference_image_path)

            # Here you would call your model processing function
            # result = process_images(source_image_path, reference_image_path)

            # processed_image_url = url_for('static', filename='results/1.png')
            # print(f'{processed_image_url}')

            return jsonify({'message': 'Files successfully processed',
                            'source': url_for('static', filename='uploads/' + source_filename),
                            'reference': url_for('static', filename='uploads/' + reference_filename)
                            })

        except Exception as e:
            current_app.logger.error(f'Error uploading files: {str(e)}')
            return jsonify({'error': 'Failed to save files'})
    return jsonify({'error': 'Unknown error'})

@main.route('/process', methods=['POST'])
def process_images():
    # Assume you receive filenames or identifiers from the frontend
    source_path = request.form.get('source')
    reference_path = request.form.get('reference')
    print(f'source_path: {source_path}; reference_path: {reference_path}')

    # Your image processing logic here
    # result_path = run_model(source_path, reference_path)
    processed_image_url = url_for('static', filename='results/1.png')
    print(f'{processed_image_url}')

    return jsonify({
         'result': processed_image_url
    })