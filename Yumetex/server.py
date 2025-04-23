# Priscilla Zhu QZ2531

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
from flask import redirect, url_for
import re
app = Flask(__name__)

blocks = {
    "1":{
        "id":"1",
        "name": "White Floral",
        "article-no": "MHG20115",
        "fabric-comp": ["40% Silk", "60% Cotton"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHG20115.png",
        "description": "Elegantly designed, substanably made silk cotton chiffon. This fabric in our signature Prints and Real Batik Collection featuress intricate patterns and natural, vibrant colors. White Floral evokes elegance, romance, and the vintage charm of the floral pattern. Freshly designed for 2026 Spring/Summer. ",
        "price": 7.5,
        "MOQ": 500
    },

    "2":{
        "id":"2",
        "name": "Black Gold",
        "article-no": "MH04079",
        "fabric-comp": ["99% Silk", "1% Lurex"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MH04079.png",
        "description": "Black gold features gold stripes shimmering on luxurious black silk. It is ideal for any high-end ready to wear clothing pieces. It is a part of our iconic Lurex Silk Mix Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 12.8,
        "MOQ": 1000
    },

    "3":{
        "id":"3",
        "name": "Black Silver",
        "article-no": "MHG24103",
        "fabric-comp": ["85% Silk", "15% Lurex"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHG24103.png",
        "description": "Want to have some mystery on your designer shirt? Black Silver provides the perfect balance of delicate intricacy and style. It is a part of our iconic Lurex Silk Mix Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 11.7,
        "MOQ": 1000
    },

    "4":{
        "id":"4",
        "name": "Pink Silver",
        "article-no": "MHJ23040",
        "fabric-comp": ["68% Silk", "32% Lurex"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHJ23040.png",
        "description": "Glittery, pastel pink whimsical. What is better than Pink Silver for the perfect blouse for a lady with a never-aging heart? It is a part of our iconic Lurex Silk Mix Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 8.7,
        "MOQ": 1000
    },

    "5":{
        "id":"5",
        "name": "Pink Star",
        "article-no": "MHJ21037",
        "fabric-comp": ["90% Silk", "10% Lurex"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHJ21037.png",
        "description": "Twinkle twinkle little star. Thin silky fabric with glistening silver star makes the dream for everyone. It is a part of our iconic Lurex Silk Mix Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 10.9,
        "MOQ": 1000
    },

    "6":{
        "id":"6",
        "name": "Grey Linen",
        "article-no": "MHA22085",
        "fabric-comp": ["100% Linen"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHA22085.png",
        "description": "The sturdy texture of Grey Linen is incomparable. Ideal for any item featuring comfortable, warmth, and style. It is a part of our most daily luxurious Linen & Hemp Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 8.3,
        "MOQ": 1000
    },

    "7":{
        "id":"7",
        "name": "White Linen",
        "article-no": "MHG10061",
        "fabric-comp": ["33% Silk", "67% Cotton"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHG10061.png",
        "description": "Cotton comfort over all, with a mix of silk for extra smoothness. Breatheable White Linen makes the perfect pair of dress shorts for summer. It is a part of our most daily luxurious Linen & Hemp Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 10.5,
        "MOQ": 1000
    },

    "8":{
        "id":"8",
        "name": "Grey Jacquard",
        "article-no": "MHJ23047",
        "fabric-comp": ["100% Silk"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHJ23047.png",
        "description": "Vibrant patterns for a casual look. This fabric highlights design with the comfort from 100% silk. It is a part of our intricate Jacquard Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 7.1,
        "MOQ": 1000
    },

    "9":{
        "id":"9",
        "name": "White Jacquard",
        "article-no": "MH06580-1",
        "fabric-comp": ["33% Silk", "55% Linen", "22% Rayon"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MH06580-1.png",
        "description": "Who says there can't be fifty shades of white? The luminous pink shade only makes this fabric more intimate. It is a part of our intricate Jacquard Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 20.0,
        "MOQ": 1000
    },

    "10":{
        "id":"10",
        "name": "White Plaid",
        "article-no": "MHA25024YS",
        "fabric-comp": ["100% Cotton"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHA25024YS.png",
        "description": "Delicate patterns with the most satisfying feel on the hands. White Plaid could be made into shirts or dresses, depending on your likes. It is a part of our gorgeous Salt Shrink Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 4.0,
        "MOQ": 1000
    },

    "11":{
        "id":"11",
        "name": "Grey Floral",
        "article-no": "MHA25029YS",
        "fabric-comp": ["100% Cotton"],
        "image": "https://raw.githubusercontent.com/priscillaz05/COMS4170-UI-Design-Yumetex/refs/heads/main/MHA25029YS.png",
        "description": "Floral, floral, floral. Beautiful patterns featuring comfort from 100% cotton. It is a part of our gorgeous Salt Shrink Collection. Freshly designed for 2026 Spring/Summer.",
        "price": 4.0,
        "MOQ": 1000
    }
}

@app.route('/')
def home_page():
    fav_blocks = [blocks["9"], blocks["6"], blocks["10"]]
    return render_template('home_page.html', blocks_len = len(blocks), blocks = blocks, fav_blocks = fav_blocks)

def highlight_text(text, query):
    text = re.sub(r'<span class="search-highlight">(.*?)</span>', r'\1', text)

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    return pattern.sub(lambda match: f'<span class="search-highlight">{match.group()}</span>', text)

@app.route('/search_results')
def search_results():
    query = request.args.get('query', '').lower()

    def match(block):
        return (
            query in block["name"].lower() or
            any(query in comp.lower() for comp in block["fabric-comp"]) or
            query in block["description"].lower()
        )

    filtered_results = [block for block in blocks.values() if match(block)]

    highlighted_results = []
    for block in filtered_results:
        highlighted_block = block.copy()
        highlighted_block['name'] = highlight_text(block['name'], query)
        highlighted_block['description'] = highlight_text(block['description'], query)
        highlighted_block['fabric-comp'] = [highlight_text(comp, query) for comp in block['fabric-comp']]
        highlighted_results.append(highlighted_block)

    return render_template('search_results.html',query=query, results=filtered_results, highlighted_results = highlighted_results)

@app.route('/view/<item_id>')
def view_item(item_id):
    print(f"Item ID received: {item_id}, Blocks keys: {list(blocks.keys())}")  # Debugging line

    item = blocks.get(item_id)
    if not item:
        return "Item not found", 404
    
    return render_template('view_item.html', item = item, blocks = blocks)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Extract data from the form
        itemname = request.form.get('itemname').strip()
        article_no = request.form.get('articleNo').strip()
        price = request.form.get('price').strip()
        MOQ = request.form.get('MOQ').strip()
        fabric_comp = request.form.get('fabricComp').strip()
        description = request.form.get('description').strip()
        fabric_image = request.form.get('fabricImage').strip()

        # Error handling (check if fields are empty)
        if not article_no or not price or not MOQ or not fabric_comp or not description or not fabric_image:
            return jsonify({"error": "All fields are required."}), 400

        # Check if price and MOQ are numbers
        if not price.isdigit() or not MOQ.isdigit():
            return jsonify({"error": "Price and MOQ must be numbers."}), 400

        # Add new block
        new_item = {
            "id": str(len(blocks) + 1),
            "name":itemname,
            "article-no": article_no,
            "price": float(price),
            "MOQ": int(MOQ),
            "fabric-comp": fabric_comp.split(','),
            "description": description,
            "image": fabric_image
        }
        blocks[new_item["id"]] = new_item

        return jsonify({"success": "Item successfully added!", "item": new_item}), 200

    return render_template('add_item.html')

@app.route('/edit/<item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = blocks.get(item_id)
    if not item:
        return "Item not found", 404

    if request.method == 'POST':
        # Get data from the form submission
        updated_name = request.form.get('name').strip()
        updated_description = request.form.get('description').strip()
        updated_price = request.form.get('price').strip()
        updated_fabric_comp = request.form.get('fabric-comp').strip()
        updated_image = request.form.get('image').strip()

        # Update the item with new data
        item['name'] = updated_name
        item['description'] = updated_description
        item['price'] = updated_price
        item['fabric-comp'] = updated_fabric_comp.split(',')  # Assuming fabric-comp is a comma-separated list
        item['image'] = updated_image

        # Redirect to the view page after updating
        return redirect(url_for('view_item', item_id=item_id))

    return render_template('edit_item.html', item=item)


if __name__ == '__main__':
   app.run(debug = True, port=5001)