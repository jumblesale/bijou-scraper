Feature: Generating data from the remote website

  @remote
  Scenario: Getting a single category from the website
    When I fetch the first category and associated products from the website
     and I convert it to json
    then I get a valid set of categories and products

#  @remote @slow
#  Scenario: Getting all categories from the website
#    When I fetch all categories and associated products from the website
