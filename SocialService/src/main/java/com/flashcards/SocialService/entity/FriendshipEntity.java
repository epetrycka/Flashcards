package com.flashcards.SocialService.entity;

import com.flashcards.SocialService.constants.SocialServiceConstants;
import jakarta.persistence.*;
import lombok.*;

@Entity
@Getter @Setter @ToString @AllArgsConstructor @NoArgsConstructor
public class FriendshipEntity extends BaseEntity {

    @EmbeddedId
    private FriendshipId id;

    @ManyToOne
    @MapsId("userId")
    private UserEntity user;

    @ManyToOne
    @MapsId("friendId")
    private UserEntity friend;

    @Column(nullable = false)
    private String status;

    public SocialServiceConstants.InvitationStatus getStatus() {
        return SocialServiceConstants.InvitationStatus.valueOf(status);
    }
}
