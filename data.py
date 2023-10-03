rules = [
      {
        "id": 1,
        "rule_name": "new_membership",
        "expression": "action_type == 'new_member'",
        "actions" : "activate_membership, send_email_to_member"
      },
      {
        "id": 2,
        "rule_name": "upgrade_membership",
        "expression": "action_type == 'upgrade'",
        "actions" : "upgrade_membership, send_email_to_member"
      },
      {
        "id": 3,
        "rule_name": "new_membership",
        "expression": "product_type == 'book'",
        "actions" : "send_email_to(royalts_email)"
      },
      {
        "id": 4,
        "rule_name": "radical_sports_videos",
        "expression": "product_type == 'video' and content_type == 'radical_sports' and media_format == 'mp4'",
        "actions" : "upgrade_membership, send_email_to_member"
      }
    ]

products = [
    {
        "id": 1, 
        "name": "O Extrangeiro", 
        "product_type": "book", 
        "product_format": "physical"
    },
    {
        "id": 2,
        "name": "aprendendo_a_esquiar.mp4", 
        "product_type": "video", 
        "product_format": "media",
        "media_name" : "aprendendo_a_esquiar",
        "media_format" : "mp4",
        "content_type" : "radical_sports" 
    },
    {
        "id": 3,
        "name": "New Membership", 
        "product_type": "membership", 
        "product_format": "online_membership"
    },
]

actions = [
    {"id" : 1, "name" : "send_email_to"},
    {"id" : 2, "name" : "gen_nota_fiscal"},
    {"id" : 3, "name" : "gen_guia_de_remessa"},
    {"id" : 4, "name" : "make_payment"},
    {"id" : 5, "name" : "activate_membership"},
]
    