Feature: Extracting product details from an individual product page

  @local
  Scenario: Getting product details from a polo-shirt page
    Given I have the example page polo-shirt.html
     when I scrape that page for product details
     then I get the product details:
      | attribute   | value                            |
      | name        | THE JUDE SHORT SLEEVE POLO SHIRT |
      | price       | £40.00                           |
      | item_number | F4KS70E6GP                       |
      | details     | Polo Shirt\nSlim Fit\nShort Sleeve\nAll Over Square Print\nConcealed Placket\nEmbroidered Farah Logo\n100% Cotton\nModel Wears Medium |
      | image_url   | http://www.farah.co.uk/dw/image/v2/AAGQ_PRD/on/demandware.static/-/Sites-perryellis_master_catalog/default/v1485756640173/products/hi-res/f4ks70e6_412.jpg |
