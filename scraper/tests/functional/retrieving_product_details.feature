Feature: Extracting product details from an individual product page

  @local
  Scenario: Getting product details from a page with no discounted price
    Given I have the example page polo-shirt.html
     when I scrape that page for product details
     then I get the product details:
      | attribute        | value                            |
      | name             | THE JUDE SHORT SLEEVE POLO SHIRT |
      | discounted_price |                                  |
      | high_price       | 40.00                            |
      | item_number      | F4KS70E6GP                       |

  @local
  Scenario: Getting product details from a page with a discounted price
    Given I have the example page long-sleeved-shirt.html
     when I scrape that page for product details
     then I get the product details:
      | attribute        | value                             |
      | name             | THE FAL LONG SLEEVE CHECKED SHIRT |
      | discounted_price |                                   |
      | high_price       | 42.00                             |
      | item_number      | 5018899787594                     |

  @local
  Scenario: Getting product details from a page with a price range
    Given I have the example page long-sleeved-shirt-with-price-range.html
     when I scrape that page for product details
     then I get the product details:
      | attribute        | value                       |
      | name             | THE KINCH LONG SLEEVE SHIRT |
      | discounted_price | 49.00                       |
      | high_price       | 70.00                       |
      | item_number      | F4WF60J6GP                  |
