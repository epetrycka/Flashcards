package com.flashcards.SocialService.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.NotEmpty;
import lombok.Data;

import java.util.List;

@Data
@Schema(
        name = "UserDto",
        description = "Schema to hold information about user"
)
public class UserDto {

    @NotEmpty(message = "User ID can not be null or empty")
    @Schema(
            description = "Unique identifier of the user",
            example = "1"
    )
    private Long id;

    @NotEmpty(message = "Username can not be null or empty")
    @Schema(
            description = "Username of the user",
            example = "user123"
    )
    private String username;

    @NotEmpty(message = "Email can not be null or empty")
    @Schema(
            description = "Email of the user",
            example = "user123@example.com"
    )
    private String email;

    private List<FriendDto> friendships;
}
