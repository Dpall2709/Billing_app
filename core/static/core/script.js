console.log("Script loaded successfully");

let itemCount = 0;

function addItemRow() {
    const table = document.getElementById('items_table').getElementsByTagName('tbody')[0];
    const row = table.insertRow();
    row.id = 'item_row_' + itemCount;

    row.innerHTML = `
        <td>
            <select name="product_${itemCount}" required>
                {% for product in products %}
                <option value="{{ product.id }}">{{ product.name }}</option>
                {% endfor %}
            </select>
        </td>
        <td><input type="number" name="bag_weight_${itemCount}" value="20" min="1" required oninput="updateLineTotal(${itemCount})"></td>
        <td><input type="number" name="bag_count_${itemCount}" value="1" min="1" required oninput="updateLineTotal(${itemCount})"></td>
        <td><input type="number" name="price_${itemCount}" value="0" min="0" required oninput="updateLineTotal(${itemCount})"></td>
        <td><span id="line_total_${itemCount}">0</span></td>
        <td><button type="button" onclick="removeItemRow(${itemCount})">Remove</button></td>
    `;

    itemCount++;
    document.getElementById('items_count').value = itemCount;
    updateTotalAmount();
}

function removeItemRow(index) {
    const row = document.getElementById('item_row_' + index);
    row.remove();
    updateTotalAmount();
}

function updateLineTotal(index) {
    const weight = parseFloat(document.getElementsByName(`bag_weight_${index}`)[0].value);
    const count = parseFloat(document.getElementsByName(`bag_count_${index}`)[0].value);
    const price = parseFloat(document.getElementsByName(`price_${index}`)[0].value);

    const total = weight * count * price;
    document.getElementById(`line_total_${index}`).innerText = total.toFixed(2);

    updateTotalAmount();
}

function updateTotalAmount() {
    let total = 0;
    for (let i = 0; i < itemCount; i++) {
        const lineTotalEl = document.getElementById(`line_total_${i}`);
        if (lineTotalEl) total += parseFloat(lineTotalEl.innerText);
    }
    document.getElementById('total_amount').innerText = total.toFixed(2);
}
