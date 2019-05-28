Feature: celestial_rootfs_install

    Scenario: update rootfs device node
        Given an ext4 formatted file
        And a target device node
        When we invoke celestial_rootfs_install
        Then the ext4 file is burned into the target device node

    Scenario: fails when given a non-ext4 formatted file
        Given a non-ext4 formatted file
        When we invoke celestial_rootfs_install
        Then the update fails
