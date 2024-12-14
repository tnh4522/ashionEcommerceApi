INSERT INTO api_permission (id, model_name, action, description) VALUES (1, 'user', 'create', 'The user is allowed to create a new user.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (2, 'user', 'read', 'The user is allowed to read user details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (3, 'user', 'update', 'The user is allowed to update user details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (4, 'user', 'delete', 'The user is allowed to delete a user.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (5, 'role', 'create', 'The user is allowed to create a new role.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (6, 'role', 'read', 'The user is allowed to read role details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (7, 'role', 'update', 'The user is allowed to update role details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (8, 'role', 'delete', 'The user is allowed to delete a role.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (9, 'permission', 'create', 'The user is allowed to create a new permission.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (10, 'permission', 'read', 'The user is allowed to read permission details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (11, 'permission', 'update', 'The user is allowed to update permission details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (12, 'permission', 'delete', 'The user is allowed to delete a permission.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (13, 'role_permission', 'assign', 'The user is allowed to assign permissions to roles.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (14, 'role_permission', 'read', 'The user is allowed to read role-permission assignments.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (15, 'role_permission', 'revoke', 'The user is allowed to revoke permissions from roles.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (16, 'user_permission', 'assign', 'The user is allowed to assign permissions to users.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (17, 'user_permission', 'read', 'The user is allowed to read user-permission assignments.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (18, 'user_permission', 'revoke', 'The user is allowed to revoke permissions from users.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (19, 'address', 'create', 'The user is allowed to create a new address.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (20, 'address', 'read', 'The user is allowed to read address details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (21, 'address', 'update', 'The user is allowed to update address details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (22, 'address', 'delete', 'The user is allowed to delete an address.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (23, 'category', 'create', 'The user is allowed to create a new category.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (24, 'category', 'read', 'The user is allowed to read category details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (25, 'category', 'update', 'The user is allowed to update category details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (26, 'category', 'delete', 'The user is allowed to delete a category.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (27, 'tag', 'create', 'The user is allowed to create a new tag.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (28, 'tag', 'read', 'The user is allowed to read tag details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (29, 'tag', 'update', 'The user is allowed to update tag details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (30, 'tag', 'delete', 'The user is allowed to delete a tag.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (31, 'product', 'create', 'The user is allowed to create a new product.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (32, 'product', 'read', 'The user is allowed to read product details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (33, 'product', 'update', 'The user is allowed to update product details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (34, 'product', 'delete', 'The user is allowed to delete a product.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (35, 'product_image', 'upload', 'The user is allowed to upload a new product image.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (36, 'product_image', 'read', 'The user is allowed to view product images.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (37, 'product_image', 'update', 'The user is allowed to update product image details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (38, 'product_image', 'delete', 'The user is allowed to delete a product image.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (39, 'cart', 'read', 'The user is allowed to view their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (40, 'cart', 'update', 'The user is allowed to update their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (41, 'cart', 'delete', 'The user is allowed to clear their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (42, 'cart_item', 'add', 'The user is allowed to add items to their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (43, 'cart_item', 'read', 'The user is allowed to view items in their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (44, 'cart_item', 'update', 'The user is allowed to update quantities of items in their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (45, 'cart_item', 'delete', 'The user is allowed to remove items from their cart.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (46, 'wishlist', 'read', 'The user is allowed to view their wishlist.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (47, 'wishlist_item', 'add', 'The user is allowed to add items to their wishlist.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (48, 'wishlist_item', 'read', 'The user is allowed to view items in their wishlist.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (49, 'wishlist_item', 'delete', 'The user is allowed to remove items from their wishlist.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (50, 'order', 'create', 'The user is allowed to place a new order.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (51, 'order', 'read', 'The user is allowed to view their orders.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (52, 'order', 'update', 'The user is allowed to update order details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (53, 'order', 'cancel', 'The user is allowed to cancel their order.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (54, 'order_item', 'read', 'The user is allowed to view items in their order.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (55, 'review', 'create', 'The user is allowed to write a review.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (56, 'review', 'read', 'The user is allowed to read reviews.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (57, 'review', 'update', 'The user is allowed to update their own reviews.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (58, 'review', 'delete', 'The user is allowed to delete their own reviews.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (59, 'coupon', 'create', 'The user is allowed to create a new coupon.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (60, 'coupon', 'read', 'The user is allowed to view coupon details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (61, 'coupon', 'update', 'The user is allowed to update coupon details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (62, 'coupon', 'delete', 'The user is allowed to delete a coupon.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (63, 'loyalty_point', 'read', 'The user is allowed to view their loyalty points.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (64, 'transaction', 'read', 'The user is allowed to view their transactions.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (65, 'message_thread', 'read', 'The user is allowed to view message threads.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (66, 'message_thread', 'delete', 'The user is allowed to delete message threads.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (67, 'message', 'send', 'The user is allowed to send messages.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (68, 'message', 'read', 'The user is allowed to read messages.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (69, 'message', 'delete', 'The user is allowed to delete messages.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (70, 'promotion', 'create', 'The user is allowed to create a new promotion.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (71, 'promotion', 'read', 'The user is allowed to view promotions.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (72, 'promotion', 'update', 'The user is allowed to update promotion details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (73, 'promotion', 'delete', 'The user is allowed to delete a promotion.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (74, 'notification', 'read', 'The user is allowed to read notifications.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (75, 'notification', 'delete', 'The user is allowed to delete notifications.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (76, 'return_request', 'create', 'The user is allowed to initiate a return request.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (77, 'return_request', 'read', 'The user is allowed to view their return requests.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (78, 'shipping_method', 'create', 'The user is allowed to create a new shipping method.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (79, 'shipping_method', 'read', 'The user is allowed to view shipping methods.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (80, 'shipping_method', 'update', 'The user is allowed to update shipping method details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (81, 'shipping_method', 'delete', 'The user is allowed to delete a shipping method.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (82, 'payment_method', 'add', 'The user is allowed to add a new payment method.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (83, 'payment_method', 'read', 'The user is allowed to view their payment methods.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (84, 'payment_method', 'update', 'The user is allowed to update their payment methods.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (85, 'payment_method', 'delete', 'The user is allowed to delete a payment method.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (86, 'seller_profile', 'create', 'The user is allowed to create a seller profile.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (87, 'seller_profile', 'read', 'The user is allowed to view seller profiles.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (88, 'seller_profile', 'update', 'The user is allowed to update seller profile details.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (89, 'seller_profile', 'delete', 'The user is allowed to delete a seller profile.');
INSERT INTO api_permission (id, model_name, action, description) VALUES (90, 'activity_log', 'read', 'The user is allowed to view activity logs.');
