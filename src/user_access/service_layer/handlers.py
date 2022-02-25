from user_access.domain import commands


def github_callback(
    cmd: commands.LoginOrSignUp, uow: AbstractUnitOfWork
):
    with uow:
        oauth_token = external_api.get_github_oauth_token(code=cmd.code)
        user_info = external_api.get_github_user_info(oauth_token)

        github_id = user_info["id"]
        exists_user = uow.github_users.get_by_github_id(github_id=github_id)

        if exists_user:
            if check_password(user_info["node_id"], exists_user.password):
                user_instance = exists_user
            else:
                raise InvalidLoginCredentialsException()
        else:
            hashed_password = hash_password(user_info["node_id"])
            user_instance = GithubUser(
                github_id=github_id,
                password=hashed_password,
                username=user_info["login"],
                avatar_url=user_info["avatar_url"],
            )
            uow.github_users.add(github_user=user_instance)

        payload = jwt_payload_handler(user_instance)
        token = jwt_encode_handler(payload)

        uow.commit()

    return SNSGithubCallbackResponseDto(token=token)
