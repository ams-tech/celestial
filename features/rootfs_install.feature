Feature: rootfs installation

    @fixture.utils.fs
    Scenario: update rootfs device node
        Given an ext4 formatted file
        And a target device node
        When we invoke rootfs device node update
        Then the ext4 file is burned into the target device node

    @fixture.utils.fs
    Scenario: fails when given a non-ext4 formatted file
        Given a non-ext4 formatted file
        When we invoke rootfs device node update
        Then the update fails
