Feature: celestial_rootfs_install

    Scenario Outline: update rootfs device node with expected fs format
        Given a rootfs file formatted with <expected_fs>
        And a target device node
        And we expect rootfs format <expected_fs>
        When we invoke celestial_rootfs_install
        Then the rootfs file is burned into the target device node

        Examples: Expected Filesystems
        | expected_fs   |
        | ext2          |
        | ext3          |
        | ext4          |


    Scenario: faults when given an improperly formatted file
        Given a rootfs file formatted with ext2
        And we expect rootfs format ext4
        When we invoke celestial_rootfs_install
        Then celestial_rootfs_install fails with ValueError
