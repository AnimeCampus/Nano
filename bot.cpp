#include <td/telegram/Client.h>
#include <td/telegram/td_api.h>

// Function to send a message with an image
void sendWelcomeMessage(td::Client& client, int64_t chatId) {
  // Prepare the input message content
  auto inputMessageContent =
      td::make_tl_object<td::td_api::inputMessagePhoto>(
          td::make_tl_object<td::td_api::inputFileLocal>("360_F_87970620_Tdgw6WYdWnrZHn2uQwJpVDH4vr4PINSc.jpg"),
          td::make_tl_object<td::td_api::formattedText>(
              "<b>Welcome to the bot!</b>\n\n"
              "Thank you for joining. Enjoy your time here!",
              td::make_tl_vector<td::tl_object_ptr<td::td_api::textEntity>>()));

  // Create the message sending action
  auto sendMessageAction =
      td::td_api::make_object<td::td_api::sendMessage>(
          chatId, 0, false, false, nullptr,
          td::make_tl_object<td::td_api::replyMarkupHideKeyboard>(),
          std::move(inputMessageContent));

  // Send the message
  client.execute(std::move(sendMessageAction));
}

int main() {
  td::Client client;

  // Set up an event handler to receive updates
  client.set_update_handler([&](td::tl_object_ptr<td::td_api::Object> update) {
    if (update->get_id() == td::td_api::updateNewMessage::ID) {
      auto new_message =
          td::move_tl_object_as<td::td_api::updateNewMessage>(update);

      // Check if the message is a new user joining the chat
      if (new_message->message_->content_->get_id() ==
          td::td_api::messageChatJoinByLink::ID) {
        auto join_message =
            td::move_tl_object_as<td::td_api::messageChatJoinByLink>(
                new_message->message_->content_);

        // Send welcome message with image to the chat
        sendWelcomeMessage(client, new_message->message_->chat_id_);
      }
    }
  });

  // Set up an event handler to handle errors
  client.set_error_handler([&](td::tl_object_ptr<td::td_api::error> error) {
    // Handle error
  });

  // Connect to the Telegram server
  client.execute(
      td::td_api::make_object<td::td_api::setTdlibParameters>(
          td::make_tl_object<td::td_api::tdlibParameters>()
              ->database_directory_("/path/to/database")
              ->use_message_database_(true)
              ->use_secret_chats_(true)
              ->api_id_(12345)  // Your API ID
              ->api_hash_("your_api_hash")
              ->system_language_code_("en")
              ->device_model_("Desktop")
              ->system_version_("Linux")
              ->application_version_("1.0")
              ->enable_storage_optimizer_(true)));

  // Log in to the bot account using the bot token
  client.execute(td::td_api::make_object<td::td_api::setAuthenticationToken>(
      "YOUR_BOT_TOKEN"));  // Replace with your bot token

  // Run the event loop
  while (true) {
    try {
      client.receive(10.0);  // Receive updates every 10 seconds
    } catch (const std::exception& e) {
      // Handle connection or other errors
      // You can log the error or perform any necessary actions
      // For simplicity, this example just
