function select_adj() {
    document.getElementById('empty').innerHTML =
        <div id="adj">
            <label htmlFor="toggle_adj" className="btn-primary">Użyj przymiotnika</label>
            <input id="toggle_adj" type="checkbox"/>
            <form id="adjective_form">
                <label htmlFor="adjective_dropdown">Wybierz przymiotnik:</label>
                <select name="adjectives" id="adjective_dropdown"></select>
                <input type="submit" value="Submit"/>
            </form>
        </div>
}