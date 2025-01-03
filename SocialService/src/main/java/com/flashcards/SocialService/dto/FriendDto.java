package com.flashcards.SocialService.dto;

import com.flashcards.SocialService.constants.SocialServiceConstants;
import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotEmpty;
import lombok.Data;

@Data
@Schema(
        name = "FriendInviteDto",
        description = "Schema to hold information about friend invitations"
)
public class FriendDto {

    @NotEmpty(message = "Sender nickname can not be null or empty")
    @Schema(
            description = "User nickname who sent the invitation",
            example = "user123"
    )
    private String senderNickname;

    @NotEmpty(message = "Recipient nickname can not be null or empty")
    @Schema(
            description = "Nickname of the invited friend",
            example = "friend456"
    )
    private String recipientNickname;

    @Schema(
            description = "Status of the invitation",
            example = "SENT"
    )
    private SocialServiceConstants.InvitationStatus status;
}
